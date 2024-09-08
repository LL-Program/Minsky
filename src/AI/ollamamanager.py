import subprocess
import sys
import platform

class OllamaManager:
    def __init__(self,main_window):
        self.os = platform.system().lower()
        self.main_window = main_window
    def run_command(self, command):
        """Utility method to run shell commands."""
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        return result.returncode == 0, result.stdout, result.stderr

    def check_and_install_ollama(self):
        """Check if ollama is installed, if not, install it based on the OS."""
        # Check if 'ollama' is installed
        is_installed, _, _ = self.run_command("ollama --version")
        
        if is_installed:
            return True
        else:
            self.main_window.Alertwidget.show_message('Ollama is not installed. Attempting to install...',5000)
        # Determine the install command based on the platform
        if self.os == 'linux':
            install_cmd = "curl -sSL https://ollama.com/download/ollama-cli-linux | sudo bash"
        elif self.os == 'windows':
            install_cmd = "Invoke-WebRequest https://ollama.com/download/ollama-cli-windows -OutFile ollama-cli.exe; .\\ollama-cli.exe"
        else:
            self.main_window.Alertwidget.show_message(f"Unsupported OS: {self.os}",5000)
            return False

        # Run the install command
        success, _, error = self.run_command(install_cmd)
        
        if success:
            self.main_window.Alertwidget.show_message("Ollama successfully installed.",5000)
            return True
        else:
            self.main_window.Alertwidget.show_message(f"Failed to install Ollama: {error}",5000)
            return False

    def install_llm_model(self, model_name):
        """Install the specified LLM model using ollama."""
        # Use the 'pull' command to install the model
        install_cmd = f"ollama run {model_name}"
    
        # Run the command and capture output
        success, output, error = self.run_command(install_cmd)
    
        # Construct the message based on the result
        if success:
            message = f"{model_name} successfully installed."
        else:
            message = f"Failed to install {model_name}"
    
    # Display the message using the GUI alert widget
        self.main_window.Alertwidget.show_message(message, 5000)
        

    def setup(self):
        """Perform the complete setup process."""
        if not self.check_and_install_ollama():
            self.main_window.Alertwidget.show_message("Cannot proceed without Ollama.",5000)
            return
        #self.install_llm_model("codellama:7b")
        self.main_window.Alertwidget.show_message("Ollama Setup Complete.",5000)