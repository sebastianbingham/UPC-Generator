# UPC Barcode Generator

This Python script generates Universal Product Code (UPC) barcodes. It prompts the user for the Number System Character, the Company Prefix, a starting Product Number, and the number of codes to generate. It calculates the check digit, generates the full UPC barcodes, and exports the data to a CSV file with a timestamp in the filename.

## How to Use

1. Make sure you have Python installed on your system.

2. Download or clone this repository to your computer.

3. Open a terminal or command prompt and navigate to the directory where the script is located.

4. Run the script by executing the following command:

5. Follow the prompts to enter the required information:
- Number System Character (single digit)
- Company Prefix (exactly 5 digits)
- Starting Product Number (exactly 5 digits)
- Number of codes to generate

6. The script will calculate the check digit, generate UPC codes, and save them to a CSV file with a timestamp in the filename (e.g., `barcodes_output_TIMESTAMP.csv`).

7. The generated UPC codes are now ready for use.

## Disclaimer

Please note that the format and usage of Universal Product Codes (UPCs) are subject to licensing and industry standards regulated by organizations like GS1. This script is provided for educational and demonstration purposes only. It is essential to adhere to industry guidelines and obtain the necessary permissions and licenses if you plan to use UPCs in a commercial or official capacity.

The script does not generate GS1-compliant UPCs with assigned company prefixes. It merely calculates check digits and combines user-provided data into UPC-like codes. Ensure compliance with applicable standards when using UPCs for commercial purposes.

## License

This script is provided under the [MIT License](LICENSE).
