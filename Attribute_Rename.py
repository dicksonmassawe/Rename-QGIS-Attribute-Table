from qgis.core import QgsProject
import random
import string

def generate_random_chars():
    # Generate three random alphabetic characters
    return ''.join(random.choices(string.ascii_uppercase, k=3))

def update_column_values(layer, column_name):
    # Start an edit session
    layer.startEditing()

    i = 1
    # Loop through each feature and update the values in the specified column
    for feature in layer.getFeatures():
        a = 'NY'
        b = generate_random_chars()
        # Replace 'NEW_VALUE' with the updated value you want to set
        new_value = f"{a}{b}{i}"  # Using f-strings for string formatting
        feature.setAttribute(column_name, new_value)
        # Commit the changes for each feature
        layer.updateFeature(feature)
        i += 1

    # Commit the changes and stop the edit session
    layer.commitChanges()

def main():
    # Replace 'FINAL NYANDIRA EDITED' with the name of your layer
    layer_name = 'FINAL NYANDIRA EDITED'
    # Replace 'COLUMN_TO_EDIT' with the name of the column you want to modify
    column_to_edit = 'NY2UR'

    # Get the layer by name
    layer = QgsProject.instance().mapLayersByName(layer_name)[0]

    # Call the function to update column values
    update_column_values(layer, column_to_edit)

# Run the main function
if __name__ == "__main__":
    main()
