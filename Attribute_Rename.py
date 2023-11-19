from qgis.core import QgsProject

# Replace 'FINAL NYANDIRA EDITED' with the name of your layer
layer_name = 'FINAL NYANDIRA EDITED'

# Get the layer by name
layer = QgsProject.instance().mapLayersByName(layer_name)[0]

# Replace 'COLUMN_TO_EDIT' with the name of the column you want to modify
column_to_edit = 'NY2UR'

# Start an edit session
layer.startEditing()

i = 1

def generate_random_chars():
    # Generate three random alphabetic characters
    random_chars = ''.join(random.choices(string.ascii_uppercase, k=3))
    return random_chars

# Loop through each feature and update the values in the specified column
for feature in layer.getFeatures():
    a = 'NY'
    b = generate_random_chars()
    # Replace 'NEW_VALUE' with the updated value you want to set
    new_value = a + b + str(i)
    # Replace 'COLUMN_TO_EDIT' with the name of the column you want to modify
    feature.setAttribute(column_to_edit, new_value)
    # Commit the changes for each feature
    layer.updateFeature(feature)
    i = i + 1

# Commit the changes and stop the edit session
layer.commitChanges()