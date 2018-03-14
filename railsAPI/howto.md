# Rails API

1. Create new app 

`
 	rails new weather
`

2. Create recording model for location and temperature

`	
	rails g model Location name
	rails g model Recording location:references temp:integer status
`

3. Setup database
`
	rake db:migrate
`

4. Set the seeds in db/seeds.rb
`rb
l = Location.create(name: "New York City")
l.recordings.create(temp:32, status:"cloudy")
`