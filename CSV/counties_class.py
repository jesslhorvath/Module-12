class County:
    def __init__(self, rank, name, pcap_income, mhouse_income, mfamily_income, pop, num_households):
        self.rank = rank
        self.county_name = name
        self.percap_income = pcap_income
        self.med_house_income = mhouse_income
        self.med_family_income = mfamily_income
        self.population = pop
        self.num_households = num_households

        