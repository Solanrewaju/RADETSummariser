#Import libraries
import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame

df = pd.read_excel(r'C:/Users/schol/OneDrive/IHVN/RADET Summariser/RADET.xlsx')
df.info()

df = df.astype({'State': np.unicode_,'LGA': np.unicode_,'DatimCode': np.unicode_,'FacilityName': np.unicode_,'PatientUniqueID': np.unicode_,
'PatientHospitalNo': np.unicode_,'ANCNoIdentifier': np.unicode_,'ANCNoConceptID': np.unicode_,'HTSNo': np.unicode_,
'Sex': np.unicode_,'AgeAtStartOfARTYears': 'Int64','AgeAtStartOfARTMonths': 'Int64','CareEntryPoint': np.unicode_,
'KPType': np.unicode_,'MonthsOnART': 'Int64','TransferInStatus': np.unicode_,'DaysOfARVRefil': 'Int64','PillBalance': 'Int64',
'InitialRegimenLine': np.unicode_,'InitialRegimen': np.unicode_,'InitialCD4Count': 'Int64','CurrentCD4Count': 'Int64',
'CurrentRegimenLine': np.unicode_,'CurrentRegimen': np.unicode_,'PregnancyStatus': np.unicode_,'GestationAgeWeeks': 'Int64',
'CurrentViralLoad(c/ml)': np.float64,'ViralLoadIndication': np.unicode_,'PatientOutcome': np.unicode_,'CurrentARTStatus': np.unicode_,
'DispensingModality': np.unicode_,'FacilityDispensingModality': np.unicode_,'DDDDispensingModality': np.unicode_,
'MMDType': np.unicode_,'CurrentAgeYears': 'Int64','CurrentAgeMonths': 'Int64','MarkAsDeseased': np.unicode_,
'RegistrationPhoneNo': np.unicode_,'NextofKinPhoneNo': np.unicode_,'TreatmentSupporterPhoneNo': np.unicode_,'BiometricCaptured': np.unicode_,
'ValidCapture': np.unicode_,'CurrentWeight(Kg)': np.float64,'TBStatus': np.unicode_,'InitialFirstLineRegimen': np.unicode_,
'InitialSecondLineRegimen': np.unicode_,'DrugDurationPreviousQuarter': 'Int64','PatientOutcomePreviousQuarter': np.unicode_,'ARTStatusPreviousQuarter': np.unicode_}
)
df.info()

df[['DateTransferredIn', 'ARTStartDate', 'LastPickupDate', 'LastVisitDate', 'InitialCD4CountDate', 'CurrentCD4CountDate', 
'LastEACDate', 'PregnancyStatusDate', 'EDD', 'LastDeliveryDate', 'LMP', 'ViralLoadEncounterDate', 'ViralLoadSampleCollectionDate', 
'ViralLoadReportedDate', 'ResultDate', 'AssayDate', 'ApprovalDate', 'PatientOutcomeDate', 'DateReturnedToCare', 
'DateOfTermination', 'PharmacyNextAppointment', 'ClinicalNextAppointment', 'DateOfBirth', 'MarkAsDeseasedDeathDate', 
'BiometricCaptureDate', 'CurrentWeightDate', 'TBStatusDate', 'INHStartDate', 'INHStopDate', 'LastINHDispensedDate', 
'TBTreatmentStartDate', 'TBTreatmentStopDate', 'LastViralLoadSampleCollectionFormDate', 'LastSampleTakenDate', 
'OTZEnrollmentDate', 'OTZOutcomeDate', 'EnrollmentDate', 'InitialFirstLineRegimenDate', 'InitialSecondLineRegimenDate', 
'LastPickupDatePreviousQuarter', 'PatientOutcomeDatePreviousQuarter']] = df[['DateTransferredIn', 'ARTStartDate', 'LastPickupDate', 'LastVisitDate', 'InitialCD4CountDate', 'CurrentCD4CountDate', 
'LastEACDate', 'PregnancyStatusDate', 'EDD', 'LastDeliveryDate', 'LMP', 'ViralLoadEncounterDate', 'ViralLoadSampleCollectionDate', 
'ViralLoadReportedDate', 'ResultDate', 'AssayDate', 'ApprovalDate', 'PatientOutcomeDate', 'DateReturnedToCare', 
'DateOfTermination', 'PharmacyNextAppointment', 'ClinicalNextAppointment', 'DateOfBirth', 'MarkAsDeseasedDeathDate', 
'BiometricCaptureDate', 'CurrentWeightDate', 'TBStatusDate', 'INHStartDate', 'INHStopDate', 'LastINHDispensedDate', 
'TBTreatmentStartDate', 'TBTreatmentStopDate', 'LastViralLoadSampleCollectionFormDate', 'LastSampleTakenDate', 
'OTZEnrollmentDate', 'OTZOutcomeDate', 'EnrollmentDate', 'InitialFirstLineRegimenDate', 'InitialSecondLineRegimenDate', 
'LastPickupDatePreviousQuarter', 'PatientOutcomeDatePreviousQuarter']].apply(pd.to_datetime)
df.info()

#df['DateOfTermination'] = pd.to_datetime(df['DateOfTermination'], errors = 'coerse')
#df.shape