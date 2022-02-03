from prescription_data import *

trial_patients = ["Denise", "Eddie", "Frank", "Georgia", "Kenny"]

for patient in trial_patients:
    prescription = patients[patient]
    if warfarin in prescription:
        # prescription.remove(warfarin)       # Kenny good :)           [without loop]
        prescription.discard(warfarin)    # Kenny dead (probably) :(    [without loop]
        prescription.add(edoxaban)
    else:
        print(f"Patient {patient} is not taking Warfarin. Check the trial list again")


print(patient, prescription)