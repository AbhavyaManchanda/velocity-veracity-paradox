import time
import random

class CalibratedAgent:
    """
    Implements the 'Calibrated Velocity' Framework.
    Adjusts execution speed and transparency logs based on Decision Importance.
    """
    
    def __init__(self, agent_name="Agentic-Exoskeleton-v1"):
        self.agent_name = agent_name
        # Importance levels determine the 'Metabolic Rate' (wait times)
        self.config = {
            "Low": {"delay": 0.5, "verbose": False},
            "Medium": {"delay": 2.0, "verbose": True},
            "High": {"delay": 4.0, "verbose": True},
            "Critical": {"delay": 6.0, "verbose": True}
        }

    def _generate_traceability_logs(self, task_name):
        """Simulates progressive disclosure of reasoning steps."""
        logs = [
            f"[Trace] Initializing reasoning core for: {task_name}",
            "[Trace] Accessing external tools and API endpoints...",
            "[Trace] Cross-referencing data veracity with trusted nodes...",
            "[Trace] Calculating confidence intervals and edge cases..."
        ]
        return logs

    def execute_task(self, task_name, importance="Medium"):
        """
        Executes a task using Calibrated Velocity.
        Calculates delay (V_c) based on Decision Importance (D_i).
        """
        setting = self.config.get(importance, self.config["Medium"])
        print(f"\n--- Starting Task: {task_name} (Importance: {importance}) ---")
        
        start_time = time.time()
        
        if setting["verbose"]:
            # Progressive Disclosure logic
            logs = self._generate_traceability_logs(task_name)
            for log in logs:
                print(log)
                # Calibrated Delay: Slowing down for transparency
                time.sleep(setting["delay"] / len(logs))
        else:
            # High Velocity for Low Stakes
            print("[Info] High-Velocity execution enabled for low-risk task.")
            time.sleep(setting["delay"])

        end_time = time.time()
        duration = end_time - start_time
        
        result = {
            "status": "Success",
            "task": task_name,
            "calibrated_duration": f"{duration:.2f}s",
            "veracity_score": random.uniform(0.85, 0.99) # Simulated accuracy
        }
        
        print(f"--- Execution Complete. Duration: {result['calibrated_duration']} ---\n")
        return result

# Example usage for testing the logic
if __name__ == "__main__":
    agent = CalibratedAgent()
    
    # 1. Low Stake Task (High Velocity)
    agent.execute_task("Draft an internal email", importance="Low")
    
    # 2. Critical Stake Task (Calibrated Velocity / Traceability)
    agent.execute_task("Rebalance $1M Portfolio", importance="Critical")