# 🔧 Visual Component Guide & Wiring Instructions

## 📦 What Each Component Looks Like

### 🎯 BBC Micro:bit
```
     ┌─────────────────────┐
     │  [ A ]  😊  [ B ]   │  ← Buttons A & B
     │                     │
     │  ● ● ● ● ●          │  ← LED Matrix (5x5)
     │  ● ● ● ● ●          │
     │  ● ● ● ● ●          │
     │  ● ● ● ● ●          │
     │  ● ● ● ● ●          │
     │                     │
     │ 0  1  2  3V GND     │  ← Edge Connector Pins
     └─────────────────────┘
```

### 🔌 2N2222 NPN Transistor (Most Important!)
```
Looking at the FLAT side with text:

    E   B   C     ← Pin names
    │   │   │
    │   │   │
  ┌─┴─┬─┴─┬─┴─┐
  │ 2N2222    │   ← Text on flat side
  │     NPN   │
  └───────────┘

E = Emitter (connect to GROUND)
B = Base (connect to Pin 0 through resistor)  
C = Collector (connect to Motor negative)
```

### ⚡ DC Motor
```
    ┌─────────┐
    │  MOTOR  │
    │    ⚙️    │  ← Shaft for rod/vibration weight
    └─────────┘
         │ │
      RED BLACK  ← Two wires
      (+) (-)
```

### 🔶 1N4007 Diode (Protection)
```
    ├────▲────┤
         │
    Silver stripe points to POSITIVE motor terminal
    (Prevents motor from damaging circuit)
```

### 🎛️ 1K Ohm Resistor
```
    ┌─[████████]─┐  ← Brown-Black-Red-Gold bands
    │            │
   PIN          PIN
```

## 🔗 Step-by-Step Visual Wiring Guide

### Step 1: Identify Transistor Pins
**CRITICAL:** Get this right or circuit won't work!

```
Hold transistor with FLAT side facing you:

┌─────────────┐
│  2N2222     │ ← Flat side with text
│    NPN      │
└─┬───┬───┬───┘
  E   B   C    ← Left to Right: Emitter, Base, Collector
```

### Step 2: Breadboard Layout
```
Micro:bit Edge Connector
        │
    ┌───▼──────────────────────────┐
    │ 0  1  2  3V GND             │
    │ │     │   │                 │  
    │ │     │   │                 │  Breadboard
    │ │  ┌──┴───┴──┐              │
    │ │  │ 1K Res  │              │
    │ │  └─────┬───┘              │
    │ │        │                  │
    │ │    ┌───▼───┐              │
    │ │    │   B   │ ← Transistor │
    │ └────┤ E   C ├──────────────┤
    │      └───────┘              │
    │                             │
    └─────────────────────────────┘
```

### Step 3: Motor Connection Points
```
                    MOTOR
                  ┌─────────┐
             RED  │  ⚙️     │  BLACK
              │   │         │   │
              │   └─────────┘   │
              │                 │
              ▼                 ▼
         [3V Power]        [To Transistor
                            Collector]
```

### Step 4: Complete Circuit Visual
```
                  MICRO:BIT
               ┌─────────────┐
               │  Pin 0      │──┐
               │             │  │
               │  3V   GND   │──┼──┐
               └─────────────┘  │  │
                                │  │
                      1K Res    │  │
                     ┌─[███]────┘  │
                     │             │
               ┌─────▼─────┐       │
      MOTOR    │ B       E │◄──────┘
    ┌────────┐ │     T     │ GND
    │   ⚙️    ├─┤ C       │
    │        │ └───────────┘
    └────────┘      ▲
         │          │
         │     ┌────┴──┐
         │     │ Diode │ ← Protection
         └─────┤  ▲│   │   (stripe toward +)
           3V  └──────┘
```

## 🎯 Physical Connection Instructions

### What Goes Where:

#### **Micro:bit Connections:**
- **Pin 0** → One end of 1K resistor
- **GND** → Transistor Emitter pin
- **3V** → Motor RED wire (positive)

#### **Transistor Connections:**
- **Base (middle pin)** → Other end of 1K resistor
- **Emitter (left pin)** → Micro:bit GND
- **Collector (right pin)** → Motor BLACK wire (negative)

#### **Motor Connections:**
- **RED wire** → Micro:bit 3V pin
- **BLACK wire** → Transistor Collector

#### **Diode Connections:**
- **Stripe end** → Motor RED wire (positive)
- **Other end** → Motor BLACK wire (negative)

## ⚠️ Common Mistakes to Avoid

### ❌ **Wrong Transistor Orientation**
```
WRONG:    │ B │ E │ C │  ← Pins mixed up
CORRECT:  │ E │ B │ C │  ← When flat side faces you
```

### ❌ **Missing Diode**
- Without diode, motor can damage your Micro:bit
- Always place diode across motor terminals

### ❌ **Wrong Motor Polarity**
- RED always goes to positive power
- BLACK goes through transistor to complete circuit

## 🧪 Testing Your Connections

### Quick Check:
1. **Power LED** on Micro:bit should light up
2. **No smoke or heat** from any components
3. **Transistor gets slightly warm** when motor runs (normal)
4. **Motor shaft turns** when code runs

### If Nothing Happens:
1. Check transistor orientation (most common issue)
2. Verify all wire connections are secure
3. Make sure diode stripe points to motor positive
4. Try the test version code first

## 🔧 Tools You Might Need

- **Breadboard or jumper wires** for connections
- **Wire strippers** if using solid core wire
- **Small screwdriver** for secure connections
- **Multimeter** (optional, for testing connections)

## 📏 Component Specifications

| Component | Value/Type | Purpose |
|-----------|------------|---------|
| Transistor | 2N2222 NPN | Motor switch |
| Resistor | 1K Ohm | Protect Micro:bit |
| Diode | 1N4007 | Protect from motor kickback |
| Motor | 3-6V DC | Vibration/rotation |

## 🎥 Visual Assembly Tips

1. **Start with power OFF** - Always build circuit first
2. **Double-check transistor** - This is the most critical part
3. **Secure all connections** - Loose wires cause problems
4. **Add diode last** - Protection component
5. **Test with short code** - Use the test version first

Ready to build? Start with identifying your transistor correctly - that's the key to success! 🚀 