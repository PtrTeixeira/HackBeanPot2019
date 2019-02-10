import time
import datetime


def format_plural(count, noun):
    if count == 1:
        return str(count) + " " + noun
    else:
        return str(count) + " " + noun + "s"


def format_timestamp(timestamp):
    seconds_ago = int(time.time() - timestamp)
    cur_dt = datetime.datetime.fromtimestamp(time.time())
    post_dt = datetime.datetime.fromtimestamp(timestamp)
    cur_weekday = cur_dt.weekday()
    post_weekday = post_dt.weekday()
    post_calendar_date = post_dt.day
    cur_month = cur_dt.month
    post_month = post_dt.month
    cur_year = cur_dt.year
    post_year = post_dt.year

    if seconds_ago < -30:  # allows for difference in clocks of 30 seconds
        raise ValueError("Given timestamp " + str(timestamp) + " is in the future")
    elif seconds_ago < 60:
        return "just now"
    elif seconds_ago < 60 * 60:
        return format_plural(int(seconds_ago / 60), "minute") + " ago"
    elif seconds_ago < 60 * 60 * 24:  # floor of the hours ago
        return format_plural(int(seconds_ago / (60 * 60)), "hour") + " ago"
    elif seconds_ago < 60 * 60 * 24 * 7:
        weekdays_ago = ((cur_weekday - post_weekday - 1) % 7) + 1
        if weekdays_ago == 1:
            return "yesterday"
        else:
            return format_plural(weekdays_ago, "day") + " ago"
    elif cur_year == post_year:
        weeks_ago = int(seconds_ago / (60 * 60 * 24 * 7))
        if weeks_ago <= 4:
            return format_plural(weeks_ago, "week") + " ago"
        else:
            months_ago = cur_month - post_month
            return format_plural(months_ago, "month") + " ago"
    else:
        months = {1: 'January',
                  2: 'February',
                  3: 'March',
                  4: 'April',
                  5: 'May',
                  6: 'June',
                  7: 'July',
                  8: 'August',
                  9: 'September',
                  10: 'October',
                  11: 'November',
                  12: 'December'}
        month_name = months[post_month]

        return "{0} {1}, {2}".format(month_name, post_calendar_date, post_year)


def format_sentence(username, caption, descriptions, timestamp, location, is_video):
    """username: username as a string without the @
           description: list of strings
       description: None if none available"""
    # video is mp4
    result = ""

    if not descriptions:
        raise ValueError("No descriptions provided")
    elif len(descriptions) == 1:
        if not is_video[0]:
            if descriptions[0] is None:
                result = ("@"
                          + username
                          + " posted a photo "
                          + format_timestamp(timestamp)
                          + ". Description is unavailable.")
            else:
                result = ("@"
                          + username
                          + " posted a photo of "
                          + descriptions[0]
                          + " "
                          + format_timestamp(timestamp) + ".")
        else:
            if descriptions[0] is None:
                result = ("@"
                          + username
                          + " posted a video "
                          + format_timestamp(timestamp)
                          + ". Description is unavailable.")
            else:
                result = ("@"
                          + username
                          + " posted a video of "
                          + descriptions[0]
                          + " "
                          + format_timestamp(timestamp) + ".")
    else:
        result = ("@"
                  + username
                  + " posted an album containing "
                  + str(len(descriptions))
                  + " items "
                  + format_timestamp(timestamp)
                  + ".")
        for i in range(len(descriptions)):
            if descriptions[i] is None:
                if not is_video[i]:
                    result += " Photo"
                else:
                    result += " Video"
                result += " description unavailable."
            else:
                if not is_video[i]:
                    result += " Photo of " + descriptions[i] + "."
                else:
                    result += " Video of " + descriptions[i] + "."

    if location is not None:
        result += " Location is " + location + "."
    if caption is None or caption == "":
        result += " No caption provided."
    else:
        result += " The caption is \"" + caption + "\""
    return result

# username, caption, descriptions, timestamp, location, is_video
def format_sentence_dict(data):
    return format_sentence(data['username'],
                           data['caption'],
                           data['descriptions'],
                           data['timestamp'],
                           data['location'],
                           data['is_video'])


# print(format_sentence('aaronpradhan1',
#                       'just chillin\'',
#                       [None,
#                        'a cat in an orange sweater',
#                        'a fir tree',
#                        None,
#                        None,
#                        'Barack Obama sitting on a chair'],
#                       1549600594,
#                       'The Oval Office',
#                       [True, False, True, True, False, True]))
#
# print(format_sentence('ptrteixeira',
#                       None,
#                       ['a group of people standing on a snowy hill'],
#                       1549676194,
#                       None,
#                       [False]))
