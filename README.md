<h1>BETAFPV LiteRadio 2 SE Radio Transmitter USB (Python)</h1>
<hr/>

<h2>Introduction</h2>
<hr/>
<p>
I wanted to control my DJI Tello drone with a BETAFPV LiteRadio 2 SE controller 
via USB connected to a computer.
So I made this small project when I had some spare time.
</p>

<h2>Installing</h2>
<hr/>
Install using `pip`:

```text
pip install literadio2-se-usb
```

<h2>Usage</h2>
<hr/>

```python
from literadio2_se_usb import LiteRadio2SeUsb

controller = LiteRadio2SeUsb()
# Do not forget to run this method before reading the control outputs
controller.setup()
# Read the control outputs
controls = controller.read_controls()
print(f'{controls.throttle}')
print(f'{controls.yaw}')
print(f'{controls.roll}')
print(f'{controls.pitch}')
print(f'{controls.sa}')
print(f'{controls.sb}')
print(f'{controls.sc}')
print(f'{controls.sd}')
```

<p>
The "read_controls" method returns the "Controls" dataclass.
Each attribute of that dataclass outputs an integer between 0 and 2047.
You can pass map_to_hundred=True to the "read_controls" method 
to change the output from -100 to 100.
</p>

<p>You can specify the vendor ID and the product ID</p>

```python
from literadio2_se_usb import LiteRadio2SeUsb

controller = LiteRadio2SeUsb(0x0483, 0x5750)
# Or
controller = LiteRadio2SeUsb(id_vendor=0x0483, id_product=0x5750)
```

<p>
Otherwise the program will try to find an appropriate device 
by its product name (by default it's "BETAFPV Joystick").
</p>
<p>You can change this product name if you want to.</p>

```python
from literadio2_se_usb import LiteRadio2SeUsb

controller = LiteRadio2SeUsb(product_string='Product string')
```
