from datetime import datetime, timedelta


def add(a: int, b: int) -> int:
    return a + b


def test_add() -> None:
    # Given: 재료를 준비합니다.
    a, b = 1, 1

    # When: 테스트 대상이 되는 함수를 호출합니다.
    result = add(a, b)  # result의 타입은 int

    # Then: When절에서 실행한 결과를 검증합니다.
    assert result == 2
    # assert result ==2 는 if not result == 2: raise AssertionError 이 뚯이다


"""
실전 문제 
택배가 언제 도착할지, 예상 배송일을 계산하는 단위 태스트
- 택배는 2영업일 이후에 도착합니다. 월요일부터 금요일까지가 영업일입니다.
- 단순화를 위해 "도서산간지역"은 고려하지 않습니다.
- 단순화를 위해 설날,추석 등의 공휴일은 고려하지 않습니다.
"""


# literal 을 스지 않고 상수를 쓰는 이유
# 2라는 숫자가 "배송일이야" 라고 배경을 모르는 사람들(미래의나,협업하는사람)에게 알려주는 역할.
# magic number : 코드 안에 의미 설명 없이 갑자기 등장하는 숫자 또는 값.
DELIVERY_DAYS = 2


def _is_holiday(day: datetime) -> bool:
    return day.weekday() >= 6


def get_eta(purchase_date: datetime) -> datetime:
    current_date = purchase_date
    remaining_days = DELIVERY_DAYS

    while remaining_days > 0:
        current_date += timedelta(days=1)
        if not _is_holiday(current_date):
            remaining_days -= 1

    return current_date


def test_get_eta_2023_12_01() -> None:
    result = get_eta(datetime(2023, 12, 1))
    assert result == datetime(2023, 12, 4)


def test_get_teat_2024_12_31() -> None:
    """
    공휴일 정보가 없어서 1월1일도 평일로 취급됩니다.
    """
    result = get_eta(datetime(2024, 12, 31))
    assert result == datetime(2025, 1, 2)


# 2024년은 윤년이라 2월29일이 있음
def test_get_eta_2024_02_28() -> None:
    result = get_eta(datetime(2024, 2, 28))
    assert result == datetime(2024, 3, 1)


# 2023년은 윤년이라 2월29일이 없음
def test_get_eta_2023_02_28() -> None:
    result = get_eta(datetime(2023, 2, 28))
    assert result == datetime(2023, 3, 2)
