# Spinning Robot Controller

A Raspberry Pi Pico-based robot controller that can rotate to face specific angles and move forward. The robot uses two motors - one for rotation and one for forward movement.

## Hardware Requirements

- Raspberry Pi Pico
- 2x DC Motors with gearboxes
- 2x L298N or similar motor driver modules
- Power supply for motors (7-12V recommended)
- Basic robot chassis

## Pin Configuration

### Motor A (Forward/Backward Movement)
- `IN1`: Pin 11
- `IN2`: Pin 12  
- `ENA`: Pin 10 (PWM)

### Motor B (Rotation)
- `IN3`: Pin 14
- `IN4`: Pin 15
- `ENB`: Pin 13 (PWM)

## Features

- **Precise Angular Positioning**: Rotate to any angle (0-360°) with shortest path calculation
- **Empirical Speed Control**: Uses calibrated duty cycle conversion for consistent wheel speeds
- **Interactive Control**: Input angles via serial console
- **Smooth Movement**: Coordinated rotation and forward movement

## Usage

1. Upload the code to your Raspberry Pi Pico
2. Connect the motors as specified in the pin configuration
3. Power on the robot
4. Open a serial console (115200 baud)
5. Enter desired angles (0-360°) to make the robot rotate and move forward

### Example Commands
```
Enter angle: 90    # Rotate to 90° and move forward
Enter angle: 270   # Rotate to 270° and move forward  
Enter angle: 0     # Rotate to 0° and move forward
```

## Technical Details

### Motor Control Algorithm
- Uses PWM duty cycles for speed control
- Duty cycle to radians/second conversion based on empirical testing
- Maximum wheel speed: ~4.22 rad/s

### Rotation Calibration
- Rotation time: 0.92 seconds per 180° at calibrated speed
- Automatically calculates shortest rotation path (-180° to +180°)

### Safety Features
- Motor stop function for safe shutdown
- Direction control via IN pin combinations
- Speed limiting to prevent motor damage

## Code Structure

- `get_duty_cycleA()`: Converts desired wheel speed to PWM duty cycle
- `spin_motorA/B()`: Controls individual motors with direction
- `stop()`: Safely stops all motors
- `move()`: Main movement function with angle calculation
- Main loop: Interactive angle input and movement execution

## Calibration Notes

The robot was calibrated with:
- Forward movement speed: 100 rad/s equivalent
- Rotation speed: Fixed duty cycle of 100,000
- Initial orientation: 180° (robot starts pointing "backward")

## Dependencies

- MicroPython firmware on Raspberry Pi Pico
- Standard MicroPython libraries: `machine`, `time`, `math`

