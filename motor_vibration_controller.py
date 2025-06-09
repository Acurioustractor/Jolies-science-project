from microbit import *
import utime

# Configuration
VIBRATION_DURATION = 300  # 5 minutes in seconds
WAIT_DURATION = 7200      # 2 hours in seconds
MOTOR_PIN = pin0          # Pin connected to motor control

def setup_motor():
    """Initialize the motor control pin"""
    MOTOR_PIN.write_digital(0)  # Start with motor off
    display.show(Image.HAPPY)   # Show ready status on LED matrix
    sleep(1000)
    display.clear()

def start_vibration():
    """Start the motor vibration"""
    display.show("V")  # Show "V" for vibrating
    MOTOR_PIN.write_digital(1)  # Turn motor on
    print("Motor started - vibrating for 5 minutes")

def stop_vibration():
    """Stop the motor vibration"""
    MOTOR_PIN.write_digital(0)  # Turn motor off
    display.clear()
    print("Motor stopped - waiting 2 hours for next cycle")

def show_countdown(remaining_time, is_vibrating=False):
    """Show countdown on LED matrix"""
    if remaining_time > 60:
        # Show hours or minutes remaining
        if is_vibrating:
            mins_left = remaining_time // 60
            display.scroll(f"V{mins_left}m", delay=100)
        else:
            hours_left = remaining_time // 3600
            display.scroll(f"W{hours_left}h", delay=100)
    else:
        # Show seconds in final minute
        display.scroll(str(remaining_time), delay=100)

def main():
    """Main program loop"""
    setup_motor()
    
    print("Motor Vibration Controller Started")
    print("Pattern: Vibrate 5 min every 2 hours")
    print("Press reset button to restart cycle")
    
    cycle_count = 0
    
    while True:
        cycle_count += 1
        print(f"\n--- Cycle {cycle_count} ---")
        
        # Wait phase (2 hours)
        print("Waiting 2 hours until next vibration...")
        wait_time_remaining = WAIT_DURATION
        
        while wait_time_remaining > 0:
            # Check for button press to skip wait (for testing)
            if button_a.was_pressed():
                print("Button A pressed - skipping to vibration")
                break
            
            # Show countdown every 30 seconds during wait
            if wait_time_remaining % 30 == 0:
                show_countdown(wait_time_remaining, is_vibrating=False)
            
            sleep(1000)  # Wait 1 second
            wait_time_remaining -= 1
        
        # Vibration phase (5 minutes)
        print("Starting vibration phase...")
        start_vibration()
        vibration_time_remaining = VIBRATION_DURATION
        
        while vibration_time_remaining > 0:
            # Check for button press to stop early (emergency stop)
            if button_b.was_pressed():
                print("Button B pressed - emergency stop")
                break
            
            # Show countdown every 10 seconds during vibration
            if vibration_time_remaining % 10 == 0:
                show_countdown(vibration_time_remaining, is_vibrating=True)
            
            sleep(1000)  # Wait 1 second
            vibration_time_remaining -= 1
        
        stop_vibration()

# Start the program
if __name__ == "__main__":
    main() 