# Taipingu (タイピング)

Add-on for Anki that allows typing practice on existing cards. Shows an additional dialogue box when reviewing a card that asks for typed input that validates against the shown content. Great for practising typing words in addition to general studying.

## Requirements

- [Anki](https://apps.ankiweb.net/) installed

## Configuration

- Put the source folder into your `Anki2/addons21/` folder.
- `Tools > Add-ons > anki-taipingu`, select `Config` and add the field name of your card that contains the relevant text you wish to test into the `trigger_fields` array.
- To find the field name of a particular card type, go to `Browse > Note Types > [Card Name]` and check which field contains the relevant text.
