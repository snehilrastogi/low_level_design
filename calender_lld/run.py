from calender.services.calendar_mgmt_service import CalendarMgmtService

events = [
    {
        "event_id": 1,
        "start_time": 1,
        "end_time": 2,
        "location": "A1",
        "owner": "O1",
        "title": "MEETING",
        "type": "MEETING"
    },
    {
        "event_id": 2,
        "start_time": 1,
        "end_time": 2,
        "location": "A1",
        "owner": "O1",
        "title": "MEETING",
        "type": "MEETING"
    },
    {
        "event_id": 3,
        "start_time": 1,
        "end_time": 2,
        "location": "A1",
        "owner": "O1",
        "title": "MEETING",
        "type": "MEETING"

    },
]

users = [
    {
        "user_id": 1,
        "accepted_events": [1, 2, 3]
    },
    {
        "user_id": 2,
        "accepted_events": [1, 2, 3]
    },
    {
        "user_id": 3,
        "accepted_events": [1, 2, 3]
    }

]

if __name__ == "__main__":
    cal_obj = CalendarMgmtService(events, users)
    cal_obj.manage_calendar()
