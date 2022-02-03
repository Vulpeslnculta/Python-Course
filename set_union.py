from prescription_data import adverse_interactions

meds_to_watch = set()

# for interaction in adverse_interactions:
#     # meds_to_watch = meds_to_watch.union(interaction)
#     # meds_to_watch.update(interaction)
#     meds_to_watch |= interaction
meds_to_watch.update(*adverse_interactions)

# print(sorted(meds_to_watch))
print(*sorted(meds_to_watch), sep='\n')
