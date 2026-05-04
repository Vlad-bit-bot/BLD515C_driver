# A dictionary for useful addresses/commands for the driver

# ── Registers ────────────────────────────────────────────────
REG_CONTROL_STATUS   = 33030  # working mode and control status
REG_COMM_POLES       = 33031  # baud rate multiplier + pole pairs
REG_STARTING_TORQUE  = 33033  # starting torque (0-255)
REG_SET_ACCELERATION = 33035  # accel (low byte) / decel (high byte), unit 10 RPM/s
REG_CURRENT_PROT     = 33036  # current protection limit
REG_BRAKE_FORCE      = 33037  # brake force (0-65535)
REG_VOLT_HIGH_ALARM  = 33038  # overvoltage alarm point (unit 0.1V)
REG_VOLT_LOW_ALARM   = 33039  # undervoltage alarm point (unit 0.1V)
REG_COMM_SPEED_SET   = 33040  # target speed in RPM
REG_PID_P            = 33041  # speed closed-loop P gain (default 64)
REG_PID_I            = 33042  # speed closed-loop I gain (default 32)
REG_PID_D            = 33043  # speed closed-loop D gain (default 0)
REG_SAVE             = 33279  # write 65535 to save settings to EEPROM
REG_GIVEN_SPEED      = 33282  # internal speed setpoint readback (RPM)
REG_ACTUAL_SPEED_GET = 33286  # actual shaft speed (RPM)
REG_MOTOR_POSITION   = 33288  # motor running position
REG_TEMP_GET         = 33281  # actual temperature
REG_VOLTAGE_GET      = 33291  # bus voltage (unit 0.1V)
REG_CURRENT_PROT_VAL = 33292  # current protection readback
REG_CURRENT_GET      = 33294  # actual current (divide by 40 for Amps)
REG_ALARM            = 33295  # alarm status bitfield (read only)

# ── Control commands (REG_CONTROL_STATUS values) ─────────────
CMD_FORWARD_RUN          = 1793   # 0x0701 — Hall, internal, closed loop, forward, run
CMD_REVERSE_RUN          = 1795   # 0x0703 — Hall, internal, closed loop, reverse, run
CMD_NATURAL_STOP         = 1792   # 0x0700 — natural stop, onboard decel ramp
CMD_BRAKE_STOP           = 1796   # 0x0704 — immediate electrical brake

# ── Alarm codes (REG_ALARM bitfield) ──────────────────
ALARM_CODES = {
    0:   "Good Execution",
    1:   "Locked rotor",
    2:   "Mean current too high",
    4:   "Hall fault",
    8:   "Power undervoltage",
    16:  "Power overvoltage",
    32:  "Peak current",
    64:  "Hardware peak current",
    128: "Temperature"
}

# ── Default configuration values ─────────────────────────────
DEFAULT_ACCEL_RPM_S  = 300    # RPM per second ramp up
DEFAULT_DECEL_RPM_S  = 800    # RPM per second ramp down
DEFAULT_START_TORQUE = 160    # higher than factory (0xA0) for heavy robot
DEFAULT_BRAKE_FORCE  = 65535  # maximum electrical braking
DEFAULT_VOLT_HIGH    = 400    # 40.0V overvoltage alarm
DEFAULT_VOLT_LOW     = 280    # 28.0V undervoltage alarm
DEFAULT_PID_P        = 64     # factory default
DEFAULT_PID_I        = 32     # factory default
DEFAULT_PID_D        = 0      # factory default

# ── Save command ─────────────────────────────────────────────
SAVE_COMMAND         = 65535  # write to REG_SAVE_PARAMETERS to persist settings
