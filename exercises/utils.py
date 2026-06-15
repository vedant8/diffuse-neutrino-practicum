import numpy as np
import pandas as pd

def generate_toy_data(n_atm=5000, n_astro=150, gamma_atm=3.7, gamma_astro=2.5, seed=42):
    """Generates a toy dataset of observed neutrino energies (in GeV)."""
    np.random.seed(seed)
    
    # Energy range: 1 TeV to 10 PeV 
    e_min, e_max = 1000.0, 10000000.0
    
    # Inverse transform sampling for power laws
    def sample_power_law(gamma, n_samples):
        u = np.random.uniform(0, 1, n_samples)
        if gamma == 1.0:
            return e_min * np.exp(u * np.log(e_max / e_min))
        else:
            return (u * (e_max**(1 - gamma) - e_min**(1 - gamma)) + e_min**(1 - gamma))**(1 / (1 - gamma))
    
    # Sample energies
    E_atm = sample_power_law(gamma_atm, n_atm)
    E_astro = sample_power_law(gamma_astro, n_astro)
    
    # Combine into a single DataFrame with truth labels
    df_atm = pd.DataFrame({'energy': E_atm, 'is_signal': 0})
    df_astro = pd.DataFrame({'energy': E_astro, 'is_signal': 1})
    
    df = pd.concat([df_atm, df_astro]).sample(frac=1, random_state=seed).reset_index(drop=True)
    return df