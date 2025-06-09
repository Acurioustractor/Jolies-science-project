# Micro:bit Motor Vibration Controller

This project creates an automated vibration system using a Micro:bit that controls a motor to vibrate every 2 hours for 5 minutes.

## 📋 What You Need

### Hardware:
- BBC Micro:bit (v1 or v2)
- Small DC motor (3-6V)
- NPN Transistor (2N2222 or similar)
- 1K Ohm resistor
- Diode (1N4007 or similar) for motor protection
- Breadboard and jumper wires
- Battery pack for Micro:bit (2 AA batteries)
- Optional: Motor driver board (L293D) for easier connection

### Software:
- Mu Editor (recommended) or Thonny
- MicroPython for Micro:bit

## 🔌 Wiring Diagram

```
Micro:bit Pin 0 ──────[1K Resistor]──────── Base of Transistor (2N2222)
                                                    │
Ground (GND) ────────────────────────────────── Emitter of Transistor
                                                    │
Motor (-) ──────────────────────────────────── Collector of Transistor
                                                    │
3V or External Power (+) ────────────────────── Motor (+)
                                                    │
                                            [Diode across motor]
                                            (prevents back EMF)
```

### Simplified Connection Steps:
1. Connect Micro:bit Pin 0 to transistor base through 1K resistor
2. Connect Micro:bit GND to transistor emitter
3. Connect motor negative wire to transistor collector
4. Connect motor positive wire to 3V (or external power source)
5. Place diode across motor terminals (stripe toward positive)

## 💾 Uploading Code to Micro:bit

### Method 1: Using Mu Editor (Recommended)
1. Download and install Mu Editor from https://codewith.mu/
2. Connect your Micro:bit via USB cable
3. Open Mu Editor and select "BBC micro:bit" mode
4. Copy the code from `motor_vibration_controller.py`
5. Paste it into Mu Editor
6. Click "Flash" button to upload to Micro:bit

### Method 2: Using Online Python Editor
1. Go to https://python.microbit.org/
2. Copy and paste the code
3. Click "Download" to get the .hex file
4. Drag the .hex file to the Micro:bit drive that appears when connected

## 🧪 Testing Your Setup

1. **Start with the test version**: Use `motor_test_version.py` first
   - Vibrates for 10 seconds every 30 seconds
   - Easier to test and debug your wiring

2. **Check connections**:
   - Micro:bit should show a happy face when starting
   - LED should show "W" during waiting periods
   - LED should show "V" during vibration periods

3. **Button controls**:
   - **Button A**: Skip waiting period (jump to vibration)
   - **Button B**: Emergency stop during vibration
   - **Reset button**: Restart the entire cycle

## 🚀 Using the Full Version

Once testing works, upload `motor_vibration_controller.py` for the full functionality:
- **Waits 2 hours** between vibrations
- **Vibrates for 5 minutes** each cycle
- Shows countdown on LED display
- Same button controls as test version

## 📊 LED Display Meanings

- **Happy face**: System ready/starting up
- **"W" + number**: Waiting mode (shows hours remaining)
- **"V" + number**: Vibrating mode (shows minutes remaining)
- **Scrolling numbers**: Countdown in final minute

## 🔧 Troubleshooting

### Motor doesn't vibrate:
- Check all wiring connections
- Verify transistor orientation
- Test motor separately with battery
- Ensure diode is correctly placed

### Micro:bit doesn't start:
- Check battery level
- Re-upload the code
- Press reset button
- Check USB connection

### Code errors:
- Make sure you're using MicroPython (not regular Python)
- Check for typos when copying code
- Verify indentation is correct

## ⚡ Power Considerations

- Micro:bit can run on battery pack (2 AA batteries)
- For stronger motors, use external power supply
- Ensure shared ground between Micro:bit and motor power
- Motor should be 3-6V DC for best results

## 🔄 Customization

You can easily modify the timing by changing these values in the code:

```python
VIBRATION_DURATION = 300  # 5 minutes (300 seconds)
WAIT_DURATION = 7200      # 2 hours (7200 seconds)
```

For example, to vibrate for 3 minutes every hour:
```python
VIBRATION_DURATION = 180  # 3 minutes
WAIT_DURATION = 3600      # 1 hour
```

## 🛡️ Safety Notes

- Always use the diode to protect against motor back EMF
- Don't exceed the Micro:bit's current limits
- Use appropriate motor size for your project
- Secure all connections before running
- Test thoroughly before leaving unattended

## 📁 File Overview

- `motor_vibration_controller.py`: Main script (2 hour / 5 min cycle)
- `motor_test_version.py`: Test script (30 sec / 10 sec cycle)
- `README.md`: This instruction file

Happy building! 🔧⚡ 