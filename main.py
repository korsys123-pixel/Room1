# ============================================================
# main.py
# 애플리케이션의 시작점 (Entry Point)
# 실행 명령어: uvicorn main:app --reload
# ============================================================

from fastapi import FastAPI
from routers.minwon import router  # 민원 처리 라우터 불러오기

# ============================================================
# FastAPI 앱 인스턴스 생성
# - title: API 문서 페이지(http://localhost:8000/docs)에 표시되는 이름
# - description: API 설명
# - version: 버전 정보
# ============================================================
app = FastAPI(
    title="민원 답변 자동생성 시스템",
    description="Claude AI를 활용한 공무원 민원 답변 초안 생성 POC",
    version="1.0.0"
)

# 민원 라우터를 앱에 등록
# → routers/minwon.py에 정의된 모든 URL 경로가 활성화됨
app.include_router(router)


# ============================================================
# 직접 실행 시 (python main.py) 서버 자동 시작
# 일반적으로는 아래 명령어로 실행합니다:
#   uvicorn main:app --reload
# ============================================================
if __name__ == "__main__":
    import uvicorn
    # host="0.0.0.0": 같은 네트워크의 다른 기기에서도 접속 가능
    # port=8000: 접속 포트 번호
    # reload=True: 코드 수정 시 자동 재시작 (개발용)
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
