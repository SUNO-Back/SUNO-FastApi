from fastapi import APIRouter

from meeting.app1.dtos.create_meeting_response import CreateMeetingResponse

edgedb_router = APIRouter(prefix="/v1/edgedb/meetings", tags=["Meeting"])
mysql_router = APIRouter(prefix="/v1/mysql/meetings", tags=["Meeting"])
# 원래는 어떤 DB를 쓰는지 URL에 적을 팔요 없다 !
# 강의에서만 이렇게 진행. 실전에서는 URl에 Db이름을 넣지 말것


@edgedb_router.post(
    path="",
    description="meeting을 생성합니다"
)
async def api_create_meeting_edgedb() -> CreateMeetingResponse:
    return CreateMeetingResponse(url_code="abc")

@mysql_router.post(
    path="",
    description="meeting을 생성합니다."
)
async def api_create_meeting_mysql() -> CreateMeetingResponse:
    return CreateMeetingResponse(url_code="abc")


