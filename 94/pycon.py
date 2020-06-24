from collections import namedtuple
import os
import pickle
import urllib.request

# prework
# download pickle file and store it in a tmp file
pkl_file = 'pycon_videos.pkl'
data = f'https://bites-data.s3.us-east-2.amazonaws.com/{pkl_file}'
tmp = os.getenv("TMP", "/tmp")
pycon_videos = os.path.join(tmp, pkl_file)
urllib.request.urlretrieve(data, pycon_videos)

# the pkl contains a list of Video namedtuples
Video = namedtuple('Video', 'id title duration metrics')


def load_pycon_data(pycon_videos=pycon_videos):
    """Load the pickle file (pycon_videos) and return the data structure
       it holds"""
    with open(pycon_videos, mode="rb") as f:
        data = pickle.load(f)

    return data


def get_most_popular_talks_by_views(videos):
    """Return the pycon video list sorted by viewCount"""
    return sorted(
        videos,
        key=lambda video: int(video.metrics['viewCount']),
        reverse=True
    )


def get_most_popular_talks_by_like_ratio(videos):
    """Return the pycon video list sorted by most likes relative to
       number of views, so 10 likes on 175 views ranks higher than
       12 likes on 300 views. Discount the dislikeCount from the likeCount.
       Return the filtered list"""
    def like_ratio(video):
        metrics = video.metrics
        like_count = int(metrics["likeCount"])
        dislike_count = int(metrics["dislikeCount"])
        view_count = int(metrics["viewCount"])
        return (like_count - dislike_count) / view_count

    return sorted(
        videos,
        key=like_ratio,
        reverse=True
    )


def get_talks_gt_one_hour(videos):
    """Filter the videos list down to videos of > 1 hour"""
    return [
        video
        for video in videos
        if "H" in video.duration
    ]


def get_talks_lt_twentyfour_min(videos):
    """Filter videos list down to videos that have a duration of less than
       24 minutes"""
    def duration_lt_24_min(video):
        duration = video.duration
        if "H" not in duration:
            return int(duration.partition("M")[0].partition("PT")[2]) < 24
        return False

    return [
        video
        for video in videos
        if duration_lt_24_min(video)
    ]