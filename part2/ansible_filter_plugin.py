
def average(list):
    """Find average of list of numbers"""
    return sum(list) / float(len(list))

class FilterModule(object):
    """Query Filter"""

    def filter(self):
        return {
            "average":average
        }

"""# Sample Ansible Playbook.yml

    -
      name: Print average marks
      hosts: localhost
      vars:
        marks:
        - 10
        - 20
        - 30
        - 40

     tasks:
        - debug:
            msg: '{{marks | average}}'
"""
