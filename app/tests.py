from django.test import TestCase
from django.core.management import call_command
from app.models import Reading

# Create your tests here.

class ImportD0010TestCase(TestCase):
    def test_import_d0010(self):
        # Sample D0010 file content
        sample_data = """HEADER|D0010
D0002	Fault Resolution Report or Request for Decision on Further Action	MRA	12/03/2024	12/03/2024
D0003	Half Hourly Advances	MRA	12/03/2024	12/03/2024
D0004	Notification of Failure to Obtain Reading	MRA	12/03/2024	12/03/2024
D0005	Instruction on Action	MRA	12/03/2024	12/03/2024
D0008	Meter Advance Reconciliation Report	MRA	12/03/2024	12/03/2024
D0010	Meter Readings	MRA	12/03/2024	12/03/2024
D0011	Agreement of Contractual Terms	MRA	12/03/2024	12/03/2024
D0012	Confirmation of the Inclusion of the Metering Point in the Reading Schedules	MRA	12/03/2024	12/03/2024
D0018	Daily Profile Data Report	BSC	12/03/2024	12/03/2024
D0019	Metering System EAC/AA Data	BSC	12/03/2024	12/03/2024
D0022	Estimated Half Hourly Data Report	MRA	12/03/2024	12/03/2024
D0023	Failed Instructions	BSC	12/03/2024	12/03/2024
D0028	Standing Profile Data Report	BSC	12/03/2024	12/03/2024
D0029	Standard Settlement Configuration Report	BSC	12/03/2024	12/03/2024
D0030	Aggregated DUoS Report	BSC	12/03/2024	12/03/2024
D0036	Validated Half Hourly Advances for Inclusion in Aggregated Supplier Matrix	MRA	12/03/2024	12/03/2024
D0039	Daily Profile Coefficient File	BSC	12/03/2024	12/03/2024
D0040	Aggregated Half Hour Data File	BSC	12/03/2024	12/03/2024
D0041	Supplier Purchase Matrix Data File	BSC	12/03/2024	12/03/2024
        """
        # Write sample data to a temporary file
        with open('sample_D0010.txt', 'w') as f:
            f.write(sample_data)

        # Call the management command to import the D0010 file
        call_command('app', 'sample_D0010.txt')
        
        # Check if the readings are imported correctly
        self.assertEqual(Reading.objects.count(),0)

        # Clean up: Delete the sample D0010 file after the test
        import os
        os.remove('sample_D0010.txt')

