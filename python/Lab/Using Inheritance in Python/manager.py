from employee import Employee

class Manager(Employee):
    meetings = []
    
    def schedule_meeting(self, invitees, meeting_time):
        meeting = {'time': meeting_time, 'invitees': invitees}
        self.meetings.append(meeting)
        self.meetings.sort(key=lambda x: x['time'])
        return self.meetings

    def run_next_meeting(self):
        # current_meeting = self.meetings[0]
        # self.meetings = self.meetings[1:]
        # return current_meeting
        return self.meetings.pop(0)



# Solution
# from employee import Employee

# class Manager(Employee):
#     def __init__(self, name, email_address, title, phone_number=None):
#         super().__init__(name, email_address, title, phone_number)
#         self.meetings = []

#     def schedule_meeting(self, invitees, time):
#         self.meetings.append({"invitees": invitees, "time": time})
#         self.meetings.sort(key=lambda m: m["time"])

#     def run_next_meeting(self):
#         return self.meetings.pop(0)