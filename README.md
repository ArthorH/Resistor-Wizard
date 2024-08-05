# Resistor values calculator for variable voltage stabilizer
Program calculates best resistor values based on this schematic:
![Resistor tree](https://github.com/user-attachments/assets/ed3e84cc-2117-4db3-9c9f-d0fbe4baebe6)


## Installation
Before installation, make sure the following dependencies are installed:
 * itertools
 * numpy

if not:

```bash
pip install itertools
```

```bash
pip install numpy
```
Copy script to folder on desktop and use:

```bash
 python .\Resistor_Wizard.py
```

## Usage
Type VREF of stabilizer
```bash
==================================================================================
Type voltage stabilizer VREF in [V]:
Vref in [V] : 1.25
```
Vref usually can be found in datasheet (1.25 is default value for most bandgap based voltage reference circuits):
![image](https://github.com/user-attachments/assets/179ae467-5ce4-4371-901c-7cb3a6d3656a)
![image](https://github.com/user-attachments/assets/6b89d7c8-09bf-42ed-863d-97c4f6687277)

Select resistor ammount and desired voltages (program will assign more weight to top values. Last value provided can be considered as "dont care" although it will affect max and min voltage):
```bash
Resistor ammount (3 or 4): 4
=================================== OK ===========================================
INPUT EXPECTED VOLTAGES
From most to least significant
Enter expected voltage no. 1: 28
Enter expected voltage no. 2: 42
Enter expected voltage no. 3: 12
Enter expected voltage no. 4: 22
Enter expected voltage no. 5: 36
Enter expected voltage no. 6: 18
Enter expected voltage no. 7: 38
=================================== OK ===========================================
```
Sit back and watch
```bash
==================== FOUND EVEN BETTER COMBINATION ========================
new best distance 683.16
for voltages 683.16
With "R1" resistor values: 1.0
With "R2" resistor values: [9.1, 6.2, 6.2]
For desired voltages   : [28.0, 42.0, 12.0, 22.0, 36.0, 18.0, 38.0]
Closest i could get is : [36.5    25.55   17.1097 17.1097 25.55   14.965  12.0899]
==========================================================================
```
Program will report when all resistor values will run out with following message:
```bash
==========================  WIZARD FINISHED ==============================
     __/\__       ________ ___  ________      
. _  \\'//       |\  _____\  \|\   ___  \
-( )-/_||_\      \ \  \__/\ \  \ \  \ \  \
 .'. \_()_/       \ \   __\\ \  \ \  \ \  \
  |   | . \        \ \  \_| \ \  \ \  \ \  \
  |mrf| .  \        \ \__\   \ \__\ \__\\ \__\
 .'. ,\_____'.       \|__|    \|__|\|__| \|__|

================           BEST COMBINATION         =====================
For desired voltages: [12.0, 28.0, 42.0]
Closest i could get is:[12.2656 27.9545 20.    ]
With "R1" resistor values: 2.2
With "R2" resistor values: [47.0, 33.0]
==========================================================================
==================================================================================
                 .----------------------.
                 |                      |
          VIN o---------   - -----------|---o--------------o  VOUT
                 |      \ ^             |   |
                 |      ---             |  .-.
                 |       |              |  |R|
                 |       |              |  |1|
                 |       |              |  '-'
                 |       |      /|      |   |
                 |       |     /+|- ----|---o------o------o
                 |       |----<  |      |   |      |      |
                 |             \-|- |   |  .-.    .-.    .-.
                 |              \|  |   |  |R|    |R|    |R|
                 |                  |   |  |2|    |3|    |4|
                 |       .--------. |   |  '-'    '-'    '-'
                 |       |  VREF  |-|   |   |      |      |
                 |       '--------'     |   |      |      |
                 |                      |   |    |/     |/
                 '-----------o----------'   |  o-|    o-|
                             |              |    |>     |>
                             |              |      |      |
                             |              |      |      |
                             |              |      |      |
                            ---            ---    ---    ---
==================================================================================
```
## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## Shout out to:
* [Evan Fosmark](mailto:evan.fosmark@gmail.com) for making the amazing [Python resistor divider calculator](https://github.com/efosmark/voltage-divider), which my script is heavily based on.
* https://www.asciiart.eu for providing ascii art

## License
Author: Artem Horiunov ArtemHoriunov@gmail.com
[MIT](https://choosealicense.com/licenses/mit/)
