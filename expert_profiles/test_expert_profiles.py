# Test ExpertProfiles

"""
Introduction: LLMs, when trained with high-quality instruction-following data, align well with human intents. 
However, the quality of the output often depends on the art of prompting. 
The paper introduces ExpertPrompting as a method to elicit better responses from LLMs by envisioning a distinguished expert agent for each specific instruction. 
[Page 1]

ExpertPrompting Framework: The method involves creating an expert identity for each instruction. 
This identity is detailed and comprehensive, covering all necessary information about the expert agent. 
The LLM then answers the instruction based on this identity. 
For example, when asked about the structure of an atom, the expert identity might be a physicist specialized in atomic structure. 
[Page 2]

Methodology: ExpertPrompting is automatic, with the expert identity produced using In-Context Learning. 
The identity is detailed and can match instructions in various domains. 
The method is also simple to implement, without the need for complex prompt templates. 
[Page 3]

Evaluation: The authors evaluated the quality of answers produced using ExpertPrompting against vanilla answers. 
Results showed that ExpertPrompting answers were preferred by 48.5% in GPT4-based evaluations. 
Additionally, the ExpertLLaMA chat assistant, trained using ExpertPrompting, outperformed other open-source chat assistants 
and achieved approximately 96% of ChatGPT's capability. [Page 4]

Conclusion: ExpertPrompting offers an augmented strategy for instructing LLMs to answer like experts. 
The method produces higher-quality answers, and the ExpertLLaMA chat assistant outperforms other open-source models. 
Future work will involve enlarging the scale of instruction data to further improve ExpertLLaMA. [Page 5]
    
"""

import unittest
from expert_profiles import ExpertProfiles


class TestExpertProfiles(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.ep = ExpertProfiles()

    def test_architecture_urban_planning(self):
        query = "I need to design an apartment building for a client in a los angeles suburb."
        results = self.ep.get_profile(query)
        assert "architect" in results

    def test_art_and_design(self):
        query = "What is the art style of the Mona Lisa?"
        results = self.ep.get_profile(query)
        assert "art" in results

    def test_business(self):
        query = "What is Relative Strength Explanation?"
        results = self.ep.get_profile(query)
        assert "analyst" in results

    def test_dentistry(self):
        query = "What is the best way to prevent cavities?"
        results = self.ep.get_profile(query)
        print(results)
        assert "dentist" in results

    def test_education(self):
        query = "What are the benefits of online learning?"
        results = self.ep.get_profile(query)
        assert "education" in results

    def test_engineering(self):
        query = "How can I design a bridge that can withstand earthquakes?"
        results = self.ep.get_profile(query)
        assert "engineer" in results

    def test_environment_and_sustainability(self):
        query = "What are some ways to reduce carbon emissions?"
        results = self.ep.get_profile(query)
        assert "environm" in results

    def test_information_science(self):
        query = "What is the difference between a database and a data warehouse?"
        results = self.ep.get_profile(query)
        assert "data" in results

    def test_kinesiology(self):
        query = "What are the benefits of stretching before exercise?"
        results = self.ep.get_profile(query)
        assert "fitness trainer" in results

    def test_law(self):
        query = "What is the statute of limitations for a personal injury claim?"
        results = self.ep.get_profile(query)
        assert "legal" in results

    def test_literature_science_arts(self):
        query = "What is the significance of the double helix structure of DNA?"
        results = self.ep.get_profile(query)
        assert "biologist" in results

    def test_medicine(self):
        query = "What are the symptoms of a heart attack?"
        results = self.ep.get_profile(query)
        assert "cardi" in results

    def test_music_theatre_dance(self):
        query = "What is the difference between a ballad and a sonata?"
        results = self.ep.get_profile(query)
        assert "music" in results

    def test_nursing(self):
        query = "What are the best practices for wound care?"
        results = self.ep.get_profile(query)
        assert "medi" in results

    def test_pharmacy(self):
        query = "What are the side effects of taking aspirin?"
        results = self.ep.get_profile(query)
        assert "medi" in results

    def test_public_health(self):
        query = "What are the risk factors for developing diabetes?"
        results = self.ep.get_profile(query)
        assert "health" in results

    def test_public_policy(self):
        query = "What is the impact of the Affordable Care Act on healthcare in the US?"
        results = self.ep.get_profile(query)
        assert "policy" in results

    def test_social_work(self):
        query = "What are the benefits of family therapy?"
        results = self.ep.get_profile(query)
        assert "family therapist" in results

    def test_communication_arts_sciences(self):
        query = "What is the role of nonverbal communication in interpersonal relationships?"
        results = self.ep.get_profile(query)
        assert "communi" in results

    def test_agriculture_natural_resources(self):
        query = "What are some sustainable farming practices?"
        results = self.ep.get_profile(query)
        assert "agric" in results


if __name__ == "__main__":
    unittest.main()
