class CreatePlaylist:

    def __init__(self):
        self.youtube_client = self.get_youtube_client()
        self.all_song_info = {}

    def get_youtube_client(self):
        pass

    def get_liked_videos(self):
        pass

    def create_playlist(self):
        """Create A New Playlist"""
        request_body = json.dumps({
            "name": "Youtube Liked Songs",
            "description": "All My Youtube Liked Songs",
            "public": True
        })

        query = "https://api.spotify.com/v1/users/{}/playlists".format(
            spotify_user_id)
        response = requests.post(
            query,
            data=request_body,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(spotify_token)
            }
        )
        response_json = response.json()

        # playlist id
        return response_json["id"]

    def get_spotify_uri(self, song_name, artist):
        pass

    def add_song_to_playlist(self):
        pass

if __name__ == '__main__':
    cp = CreatePlaylist()
    cp.add_song_to_playlist()