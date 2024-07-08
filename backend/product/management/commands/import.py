import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import transaction

from product.models import Product

DATA_ROOT = os.path.join(settings.BASE_DIR, 'data')


class Command(BaseCommand):
    """
    Custom Django management command to import product data from a CSV file.

    This command reads product data from a specified CSV file and populates
    the Product model in the database.
    """

    help = 'Import data from csv file.'

    def add_arguments(self, parser):
        """
        Define the command-line arguments for this command.

        Args:
            parser (argparse.ArgumentParser): The argument parser instance.
        """

        parser.add_argument('filename',
                            default='products.csv',
                            nargs='?',
                            type=str)

    def handle(self, *args, **options):
        """
        The main logic for the command to handle the CSV data import.

        Args:
            *args: Variable length argument list.
            **options: Arbitrary keyword arguments containing command-line options.
        """

        filename = options['filename']
        filepath = os.path.join(DATA_ROOT, filename)

        try:
            # List to collect Product instances to be created
            products_list = []

            # Open the CSV file for reading
            with open(filepath, 'r', encoding='utf-8') as file:
                data = csv.reader(file)
                next(data)  # Skip the header row

                # Iterate through each row in the CSV file
                for row in data:
                    name, measurement_unit = row
                    product = Product(
                        name=name,
                        measurement_unit=measurement_unit)
                    products_list.append(product)

            # Perform a bulk create operation within a database transaction
            with transaction.atomic():
                Product.objects.bulk_create(products_list)

            # Output success message to the console
            self.stdout.write(
                self.style.SUCCESS(f'Data from {filename} has been imported successfully.'))

        except FileNotFoundError:
            # Output error message if the CSV file is not found
            self.stderr.write('CSV file not found')


"""
Explanation:

1. **Imports**:
   - `csv` and `os`: Standard Python modules for CSV file handling and path operations.
   - `settings`, `BaseCommand`, and `transaction`: Django modules for configuration, custom management commands, and database transactions.
   - `Product`: The Django model representing products.

2. **DATA_ROOT**:
   - Defines the directory where the CSV files are located.

3. **Command Class**:
   - Inherits from `BaseCommand` to create a custom management command.

4. **help Attribute**:
   - Provides a short description of what the command does.

5. **add_arguments Method**:
   - Adds a command-line argument `filename` with a default value of `products.csv`.

6. **handle Method**:
   - Contains the main logic to process the CSV file.
   - Constructs the file path from the provided filename.
   - Opens the CSV file and reads its contents.
   - Skips the header row using `next(data)`.
   - Iterates through each row in the CSV, creating `Product` instances.
   - Uses `bulk_create` within a transaction to insert all products efficiently.
   - Outputs success or error messages to the console.
"""
