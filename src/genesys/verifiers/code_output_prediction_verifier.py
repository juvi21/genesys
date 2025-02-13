from genesys.utils import extract_json
from genesys.schemas import Response
from genesys.verifiers.base_verifier import BaseVerifier


class CodeUnderstandingVerifier(BaseVerifier):
    max_parallel = 30
    timeout = 20

    def verify(self, result: Response):
        """
        Verifies whether the output predicted by the LLM matches the ground truth.

        Args:
            result (dict): A dictionary containing:
                - "llm_response": the LLM's response (expected to contain JSON data)
                - "verification_info": a dictionary with a "ground_truth" key

        Returns:
            int: 1 if the extracted output matches the ground truth, 0 otherwise.
        """
        response = result["llm_response"]
        ground_truth = result["verification_info"]["ground_truth"]

        output_prediction = extract_json(response)["output"]

        return dict(score=int(output_prediction == ground_truth), verification_result_info={})
