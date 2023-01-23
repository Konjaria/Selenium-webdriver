from datetime import datetime, timedelta


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, from_country_code="TBS", to_country_code="PAR"):
        pseudo_tomorrow = datetime.now() + timedelta(days=1)
        pseudo_six_month_later = datetime.now() + timedelta(days=180)
        self.tomorrow = pseudo_tomorrow.strftime("%d/%m/%Y")
        self.six_month_later = pseudo_six_month_later.strftime("%d/%m/%Y")
        self._from_code_ = from_country_code
        self._to_code_ = to_country_code
        self._currency_ = "GEL"
