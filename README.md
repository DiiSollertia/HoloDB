# HoloDB
A relational database of Hololive talent focused on organizing published music. Also personal database design practice. My aim is to learn how to write SQL scripts and publish SQL projects like the open source Chinook Database.

### ERD
Entity relationship diagram depicting the database schema. Keys and fields are specified.

### MEMBERS
**MEMBERS** are defined as individual talents working in the Vtuber agency **hololive production** while having personal YouTube channels  
- `id` *(Primary Key)* - sequential identifier  
- `name` - official English names of the talent  
- `status` - enum field reflecting graduation status (`0 - GRADUATED; 1 - ACTIVE; 2 - SPECIAL`)  
- `debut_gen` - generation when the talent first debuted their characters
- `debut_date` *(Sort Key)* - date when the talent first debuted their characters
- `grad_date` - date when the talent retired their characters
- `yt_channel_id` - identifier representing the talent's main YouTube channel, accessed via the URL *https<span>://ww</span>w.youtube.com/channel/`yt_channel_id`*  
- `yt_topic_id` - identifier representing the talent's YouTube Music channel (if available), accessed via the same URL as above or *https<span>://musi</span>c.youtube.com/channel/`yt_topic_id`*  
- `spotify_id` - identifier representing the talent's main Spotify artist page, accessed via the URL *https<span>://ope</span>n.spotify.com/artist/`spotify_id`*  
- `twitter_id` - identifier representing the talent's main Twitter account, accessed via the URL *https<span>://ww</span>w.twitter.com/`twitter_id`*  
- `add_notes` - additional notes providing alternate values for any of the fields that are relevant to music

### GROUPS
**GROUPS** are defined as channels on Spotify or YouTube that represent several **MEMBERS** 
- `id` *(Primary Key)* - sequential identifier with the prefix `G` to enable combination with `member_id` to form `talent_id`  
- `name` - official English names of the channels  
- `yt_channel_id` - similar as in **MEMBERS**  
- `yt_topic_id` - similar as in **MEMBERS**  
- `spotify_id` - similar as in **MEMBERS**
- `twitter_id` - similar as in **MEMBERS**

### GROUP_MEMBER
Associative entity to handle the many-to-many relationship between **GROUPS** and **MEMBERS**
- `group_id` *(Foreign Key)* - `id` from **GROUPS**  
- `member_id` *(Foreign Key)* - `id` from **MEMBERS** 

### ALBUMS
**ALBUMS** are defined as original music albums, cover albums, EPs or other collections containing 3 or more main and unique tracks released by, or in collaboration with, **MEMBERS** excluding collections that have been officially defined as Singles
- `id` *(Primary Key)* - similar as in **MEMBERS**
- `title` - titles of the **ALBUMS** as formatted on official platforms  
- `release_date` *(Sort Key)* - earliest release date of the full collection; differs from sale/retail date unless defined by official distributors as the release date
- `tracks` - number of main tracks included within the collection; bonus tracks and instrumental tracks are excluded
- `trailer_id` - identifier representing the collection trailer or preview video, most conviniently accessible via the URL *https<span>://yout</span>u.be/`trailer_id`*  
- `playlist_id` - identifier representing the YouTube playlist or YouTube Music album *(defined by the prefix `OLAK5uy_`)*, accessible via the URL *https<span>://ww</span>w.youtube.com/playlist?list=`playlist_id`* or *https<span>://musi</span>c.youtube.com/playlist?list=`playlist_id`*  
- `spotify_id` - identifier representing the Spotify album, accessible via the URL *https<span>://ope</span>n.spotify.com/album/`spotify_id`*

## To do
- SQL DB Project;  
- Google Sheets with readability prioritized;  
- CSVs for original music published on YouTube and Spotify;  
- Try to source for privated/deleted/otherwise commonly unavailable original music;  
- Create a by year compilation video of original music for documentational and promotional purposes;  
- Provide published Google Sheets link for accessability; 
- Create REST API to provide data 

## Special Thanks
Cover Corp for creating hololive production  
joexyz on Discord for advice on database schema  
[Completely Unofficial Civia Archive Channel](https://www.youtube.com/channel/UCIrO3R_SG3TZhXvzMhOP7jw) for upload information on Civia videos  
[Noctuural](https://www.youtube.com/channel/UCkutxM09u8z7M2rJiL5szsQ) for reuplaods and upload information on Yogiri videos  
All information was obtained from publically available resources, some of the more useful sites include the [official hololive production website](https://hololive.hololivepro.com/en/), [hololive fan wiki](https://hololive.wiki/wiki/Main_Page), [hololive fandom wiki](https://virtualyoutuber.fandom.com/wiki/Hololive), [Moe Girl Pedia](zh.moegirl.org.cn) etc. 

## Potential issues
- Sensitive information in django files are not stored in environment variables
- Unclear naming and definition conventions for `EVENTS`
- Unclear definition for affiliated staff members under `TALENTS` (For example Ui-sensei has Live2D and a YouTube channel, does she qualify? Currently the stance is no.)
