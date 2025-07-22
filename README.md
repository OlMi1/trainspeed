# trainspeed
Calculates the average maximum speed of trains in any given country based on OSM overpass data.
## Usage
1. Paste the Overpass command into [Overpass Turbo](https://overpass-turbo.eu/), replacing COUNTRY with the two digit code of your country of choice (US, DE, CN - located in the .py file)
2. Run the query and wait for a result
3. Once done, click "Export"
4. Choose "Raw OSM Data" and wait for your file ("export.json") to finish downloading
5. Copy the full path and enter it on line 18
6. Create a JSON file for the resulting data. Enter its path on line 19
7. Start the process and wait for the script to finish
8. Check the result file - voila!
## Notes
The script does not care for how long any given route is. It also ignores nodes. To deliver accurate numbers, it would have to consider the route length. For example, I'm assuming slower side tracks are given a higher weight in the average / median calculations as there's more of them as opposed to high speed main tracks.
Feel free to create a pull request with that change included.
