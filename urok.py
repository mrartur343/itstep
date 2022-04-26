import warnings

warnings.simplefilter("ignore",SyntaxWarning)
warnings.simplefilter("error",ImportWarning)

warnings.warn("Warning,no code here",SyntaxWarning)
warnings.warn("Warning,modyle no import",ImportWarning)
