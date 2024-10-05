import json
from astropy.io.votable import parse

def votable_to_json(votable_path, json_path):
    # Parse the VOTable file
    votable = parse(votable_path)
    table = votable.get_first_table().to_table()

    # Extract the columns
    name = table['MAIN_ID']
    dist = table['ANG_DIST']
    dec = table['DEC_d']
    ra = table['RA_d']

    # Create a list of dictionaries
    data = []
    for i in range(len(name)):
        data.append({
            'name': str(name[i]),  # Convert to string
            'dist': float(dist[i]),  # Convert to float
            'dec': float(dec[i]),  # Convert to float
            'ra': float(ra[i])  # Convert to float
        })
    
    # Write the data to a JSON file
    with open(json_path, 'w') as f:
        json.dump(data, f, indent=4)

# Example usage
listoffile = ["55Cncc","61virb"]
listofjson = ["55Cncc.json","61virb.json"]

for i in range(len(listoffile)):
    votable_to_json(listoffile[i],"stars/"+listofjson[i])