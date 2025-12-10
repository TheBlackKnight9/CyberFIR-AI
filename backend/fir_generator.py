from datetime import datetime

def generate_fir(user_name, city, incident, crime, sections):
    return f"""
To,
The In-charge,
Cyber Crime Police Station,
{city}

Subject: FIR regarding {crime}

Respected Sir/Madam,

I, {user_name}, resident of {city}, want to file a complaint regarding a cyber incident. 
Incident Description: {incident}

As per preliminary assessment, the incident falls under {crime}, 
punishable under {', '.join(sections)}.

I request you to kindly register my complaint and initiate necessary legal action.

Date: {datetime.now().strftime('%d-%m-%Y')}

Yours Faithfully,
{user_name}
"""
