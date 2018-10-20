FuzzyModbus v0.1
=====================
Modbus TCP Register Fuzzing and DoS Tool.

Install and Usage:
-------------
$> git clone https://github.com/imertayak/FuzzyModbus.git && cd FuzzyModbus

$> pip install -r requirements.txt

$> chmod +x FuzzyModbus.py

$> ./FuzzyModbus.py [OPTIONS]

### Command line options:

```
-h or --help	Help Menu

-f or --func-code <Code> Modbus Function Code
(3=ReadHoldingRegisters,6=WriteSingleRegister,10=WriteMultipleRegisters)

-F or --flood	OPTIONAL Modbus Flood/DoS Attack

-t or --target <IP_Addr>	Target Modbus Server IP Address

-p or --port <Port>	DEFAULT=502 Target Modbus Server Port

-u or --uid <UID>	DEFAULT=1 Unit ID

-a or --address <Reg_Addr>	DEFAULT=0 First Register Address

-c or --count <Count>	DEFAULT=1 Count of Registers to read/write 

```
