# 🛒 Component Shopping & Identification Guide

## 🎯 Exactly What to Buy & What They Look Like

### 1. 🎛️ BBC Micro:bit v2
**What to look for:**
- Small computer board (about credit card size)
- 5x5 LED matrix on front
- Two buttons (A & B)
- Gold edge connector pins at bottom

**Where to buy:**
- Amazon, SparkFun, Adafruit, local electronics stores
- **Price range:** $15-20

### 2. ⚡ 2N2222 NPN Transistor (MOST CRITICAL!)
**What to look for:**
```
   ┌─────────┐
   │ 2N2222  │ ← Text printed here
   │   NPN   │
   └─┬──┬──┬─┘
     │  │  │   ← 3 metal legs
```

**Package types:**
- **TO-92 package** (plastic, 3 legs) - RECOMMENDED
- Black or gray plastic body
- Text says "2N2222" or "PN2222"

**Where to buy:**
- Electronics stores, Amazon, eBay
- **Price:** $0.50-2.00 each
- **Alternative:** Any NPN transistor (BC337, 2N3904)

### 3. 🎛️ 1K Ohm Resistor
**What to look for:**
```
Color bands (left to right):
┌─[Brown][Black][Red][Gold]─┐
│                            │
└────────────────────────────┘
```

**Specifications:**
- **Brown-Black-Red-Gold** bands
- 1/4 watt or 1/2 watt (size doesn't matter much)
- Two wire leads

**Where to buy:**
- Electronics stores, Amazon (resistor packs)
- **Price:** $0.10 each or $5 for 100-pack

### 4. 🔶 1N4007 Diode
**What to look for:**
```
┌──────[████████]──────┐
│      Gray/Black      │ ← Body
│         │            │
│    Silver stripe     │ ← IMPORTANT marker
└──────────────────────┘
```

**Key features:**
- Small cylindrical component
- **Silver or white stripe** on one end
- Two wire leads
- Body says "1N4007" (tiny text)

**Where to buy:**
- Electronics stores, Amazon
- **Price:** $0.20 each
- **Alternative:** Any rectifier diode (1N4001-1N4007)

### 5. 🔄 Small DC Motor (3-6V)
**What to look for:**
```
     ┌─────────────┐
     │    MOTOR    │ ← Cylindrical metal can
     │             │
     │      ⚙️      │ ← Shaft sticking out
     └─────────────┘
          │    │
        RED  BLACK  ← Two wires
```

**Specifications:**
- 3V to 6V DC operation
- Small hobby motor (not servo motor)
- Two wires (red positive, black negative)
- Metal can body

**Types that work:**
- **Small hobby motor**
- **Vibration motor** (phone vibrator motor)
- **Gearbox motor** (slower but stronger)

**Where to buy:**
- Electronics stores, Amazon, SparkFun
- **Price:** $3-10

### 6. 🔌 Connection Materials

#### **Option A: Breadboard Setup**
- **Half-size breadboard** ($5-10)
- **Jumper wires** (male-to-male, pack of 20+) ($3-5)
- **Micro:bit breakout board** ($10-15)

#### **Option B: Direct Wiring**
- **Alligator clips** with wires ($5-10)
- **Wire strippers** ($5-10)
- **Electrical tape** ($2-3)

### 7. 🔋 Power Supply Options

#### **For Micro:bit:**
- **USB cable** (micro-USB) - usually included
- **2x AAA battery pack** with JST connector ($5-8)
- **Power bank** (portable USB charger)

#### **For Motor (Optional):**
- **4x AA battery pack** (6V for stronger motors) ($5-10)
- **9V battery** with connector (for more power) ($3-5)

## 🏪 Where to Shop

### **Online (Best Prices):**
- **Amazon** - Fast shipping, good for complete kits
- **SparkFun** - Quality components, educational focus
- **Adafruit** - Great tutorials and documentation
- **Digi-Key** - Professional components
- **eBay** - Cheap components (longer shipping)

### **Local Stores:**
- **Radio Shack** (if still open)
- **Fry's Electronics**
- **Local electronics/computer stores**
- **University bookstores** (engineering schools)

## 📦 Complete Shopping List & Budget

### **Budget Option (~$25):**
- Micro:bit: $16
- 2N2222 transistor: $1
- 1K resistor: $0.50
- 1N4007 diode: $0.50
- Small DC motor: $4
- Alligator clips: $3
- **Total: ~$25**

### **Professional Option (~$45):**
- Micro:bit: $16
- Micro:bit breakout board: $12
- Breadboard: $7
- Jumper wires: $3
- Component kit (resistors, transistors, diodes): $7
- **Total: ~$45**

## 🔍 Component Identification Tips

### **At the Store:**
1. **Ask for help** - Show this guide to store employees
2. **Look for beginner kits** - Often include all needed components
3. **Check voltage ratings** - Motor should be 3-6V DC
4. **Verify transistor type** - Must be NPN (not PNP)

### **Online Shopping:**
1. **Read descriptions carefully** - Check voltage and current ratings
2. **Look at customer photos** - See what you're actually getting
3. **Check compatibility** - Search "micro:bit motor control" in product reviews
4. **Buy extra components** - Transistors and resistors are cheap insurance

## ⚠️ Things to Avoid

### **Wrong Components:**
- ❌ **Servo motors** (different type - has 3 wires with control signal)
- ❌ **Stepper motors** (too complex for this project)
- ❌ **AC motors** (household voltage - dangerous!)
- ❌ **PNP transistors** (won't work with our circuit)

### **Common Shopping Mistakes:**
- ❌ Forgetting the diode (motor protection)
- ❌ Wrong resistor value (too high or too low)
- ❌ Motor voltage too high (will damage Micro:bit)
- ❌ No breadboard or connection method

## 💡 Money-Saving Tips

1. **Buy component kits** - Often cheaper than individual parts
2. **Check school electronics labs** - May have spare components
3. **Join maker spaces** - Access to tools and components
4. **Buy in bulk with friends** - Share the cost
5. **Start simple** - Use alligator clips before investing in breadboards

Ready to shop? Print this guide and you'll know exactly what to look for! 🛍️ 