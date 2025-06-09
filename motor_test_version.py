from microbit import *
import utime

# TEST Configuration - shorter durations for testing
VIBRATION_DURATION = 10   # 10 seconds for testing (instead of 5 minutes)
WAIT_DURATION = 30        # 30 seconds for testing (instead of 2 hours)
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
    print("Motor started - vibrating for test duration")

def stop_vibration():
    """Stop the motor vibration"""
    MOTOR_PIN.write_digital(0)  # Turn motor off
    display.clear()
    print("Motor stopped - waiting for next test cycle")

def show_countdown(remaining_time, is_vibrating=False):
    """Show countdown on LED matrix"""
    if is_vibrating:
        display.scroll(f"V{remaining_time}", delay=80)
    else:
        display.scroll(f"W{remaining_time}", delay=80)

def main():
    """Main program loop - TEST VERSION"""
    setup_motor()
    
    print("Motor Test Controller Started")
    print("TEST: Vibrate 10 sec every 30 sec")
    print("Press reset button to restart")
    
    cycle_count = 0
    
    while True:
        cycle_count += 1
        print(f"\n--- Test Cycle {cycle_count} ---")
        
        # Wait phase (30 seconds for testing)
        print("Waiting 30 seconds until next vibration...")
        wait_time_remaining = WAIT_DURATION
        
        while wait_time_remaining > 0:
            # Check for button press to skip wait
            if button_a.was_pressed():
                print("Button A pressed - skipping to vibration")
                break
            
            # Show countdown every 5 seconds during wait
            if wait_time_remaining % 5 == 0:
                show_countdown(wait_time_remaining, is_vibrating=False)
            
            sleep(1000)  # Wait 1 second
            wait_time_remaining -= 1
        
        # Vibration phase (10 seconds for testing)
        print("Starting vibration phase...")
        start_vibration()
        vibration_time_remaining = VIBRATION_DURATION
        
        while vibration_time_remaining > 0:
            # Check for button press to stop early
            if button_b.was_pressed():
                print("Button B pressed - emergency stop")
                break
            
            # Show countdown every second during vibration
            show_countdown(vibration_time_remaining, is_vibrating=True)
            
            sleep(1000)  # Wait 1 second
            vibration_time_remaining -= 1
        
        stop_vibration()

# Start the program
if __name__ == "__main__":
    main() 