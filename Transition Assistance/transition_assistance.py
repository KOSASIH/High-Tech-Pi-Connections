class TransitionAssistance:

    def __init__(self, existing_skills, desired_skills):
        """
        Create a new instance of the TransitionAssistance class.

        :param dict existing_skills: A dictionary of existing skills, with skill name as keys and levels as values.
        :param dict desired_skills: A dictionary of desired skills for the new role, with skill name as keys and levels as values.
        """

        self.existing_skills = existing_skills
        self.desired_skills = desired_skills

    def assess_transition_needs(self):
        """
        Assess the transition needs for a person based on their existing skills and desired skills for the new role.

        :return tuple (list, dict): Returns a list of skills to be gained, and a dictionary of cross-skills that can be useful during the transition.
        """

        skills_to_gain = []
        cross_skills = {}

        for skill, level in self.desired_skills.items():
            if skill not in self.existing_skills or self.existing_skills[skill] < level:
                skills_to_gain.append(skill)

        relevant_skills = set(self.existing_skills.keys()).intersection(set(self.desired_skills.keys()))
        for skill in relevant_skills:
            if self.existing_skills[skill] >= self.desired_skills[skill]:
                cross_skills[skill] = self.existing_skills[skill] - self.desired_skills[skill]

        return skills_to_gain, cross_skills


if __name__ == "__main__":

    existing_skills = {
        "Python": 1,
        "Machine Learning": 2,
        "Data Visualization": 3,
    }

    desired_skills = {
        "Python": 3,
        "Deep Learning": 2,
        "Cloud Computing": 1,
    }

    transition_assistance = TransitionAssistance(existing_skills, desired_skills)

    skills_to_gain, cross_skills = transition_assistance.assess_transition_needs()

    print(f"Skills to gain: {skills_to_gain}")
    print(f"Cross skills: {cross_skills}")
