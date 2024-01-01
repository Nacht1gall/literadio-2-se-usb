from typing import Optional, Sequence

import usb.core

from literadio2_se_usb.utils.data import Controls
from literadio2_se_usb.utils.exceptions import DeviceNotFound, InvalidEndpointAddress
from literadio2_se_usb.utils.tools import array_to_integer, map_from_to


class LiteRadio2SeUsb:
    def __init__(self, id_vendor: Optional[int] = None, id_product: Optional[int] = None,
                 product_string: str = 'BETAFPV Joystick'):
        self.id_vendor = id_vendor
        self.id_product = id_product
        self.product_string = product_string

        self.device = None
        self.endpoint_address = None

    def setup(self) -> None:
        self.device = self.find_device()
        if self.device is None:
            raise DeviceNotFound

        # Setup the required endpoint address
        interfaces = self.device[0].interfaces()
        endpoints = interfaces[0].endpoints()
        ep = endpoints[0]
        interface_number = interfaces[0].bInterfaceNumber
        self.endpoint_address = ep.bEndpointAddress

        self.device.reset()  # reset whatever is currently running on the device
        # If something is listening to the USB data from the device then stop it
        if self.device.is_kernel_driver_active(interface_number):
            self.device.detach_kernel_driver(interface_number)
        self.device.set_configuration()

    def find_device(self) -> Optional[usb.core.Device]:
        if self.id_vendor is not None or self.id_product is not None:
            return usb.core.find(idVendor=self.id_vendor, idProduct=self.id_product)

        # Try to find the controller by its product name
        for device in usb.core.find(find_all=True):
            product_string = usb.util.get_string(device, device.iProduct)
            if product_string == self.product_string:
                return device

    def read_controls(self, map_to_hundred: bool = False) -> Controls:
        if self.endpoint_address is None:
            raise InvalidEndpointAddress

        # This function receives an "array" object
        # but any sequences like lists are fine too
        def raw_data_to_number(byte_array: Sequence) -> int:
            value = array_to_integer(byte_array)
            if map_to_hundred:
                value = map_from_to(value, 0, 2047, -100, 100)
            return value

        data = self.device.read(self.endpoint_address, 16)

        roll = raw_data_to_number(data[0:2])
        pitch = raw_data_to_number(data[2:4])

        throttle = raw_data_to_number(data[4:6])
        yaw = raw_data_to_number(data[6:8])

        sa = raw_data_to_number(data[8:10])
        sb = raw_data_to_number(data[10:12])
        sc = raw_data_to_number(data[12:14])
        sd = raw_data_to_number(data[14:16])

        controls = Controls(
            roll=roll, pitch=pitch,
            throttle=throttle, yaw=yaw,
            sa=sa, sb=sb,
            sc=sc, sd=sd
        )

        return controls
