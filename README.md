# Anki-Taipingu (タイピング/Typing)

Add-on for Anki that adds quick typing tests to any card. Shows an additional dialogue box when reviewing a card that asks for typed input that validates against the shown content. Great for practising typing words in addition to general studying.

## Requirements

- [Anki](https://apps.ankiweb.net/) installed

## Installation

- **If installing via package download:** Put the source folder into your `Anki2/addons21/` folder.
- **If installing via AnkiWeb:** `Tools > Add-ons > Get Add-ons...` and enter the code `1818995561`

## Configuration

- `Tools > Add-ons > anki-taipingu`, select `Config` and add the field name of your card that contains the relevant text you wish to test into the `trigger_fields` array.
- To find the field name of a particular card type, go to `Browse > Note Types > [Card Name]` and check which field contains the relevant text.

## Usage

Taipingu will display a dialogue upon every new card. Type the associated word and press `Enter` to check correctness. If it is correct, press `Enter` again to close the dialogue. If you are able to get it right and wish to close the dialogue, press `Esc`.

<p align="center">
<img width="640" alt="default" src="https://github.com/kk-min/anki-taipingu/assets/76023265/ca5d4115-6844-4489-ad4b-b6751727a719">
<img width="640" alt="incorrect" src="https://github.com/kk-min/anki-taipingu/assets/76023265/b5779579-f96f-4a30-80da-8a8282adc6a9">
<img width="640" alt="correct" src="https://github.com/kk-min/anki-taipingu/assets/76023265/ce330edf-a10e-4330-9b28-e3750a4436d9">
</p>

Taipingu can be enabled/disabled via `Tools > Taipingu > Enable typing test`.

## Acknowledgements

- [fsrs4anki-helper](https://github.com/open-spaced-repetition/fsrs4anki-helper)
