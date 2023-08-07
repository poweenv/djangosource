// 하단의 페이지 나누기 영역 클릭 시
// href 값 가져오기

document.querySelector("ul.pagination").addEventListener("click",(e)=>{
    e.preventDefault();
    if(e.target.tagName ==="A"){
        const href = e.target.getAttribute("href");
        document.querySelector("#page").value = href;
        document.querySelector("#actionForm").submit();
    }
});

// 검색
// 찾기 버튼 클릭 시
// 검색어 입력 여부 확인하기
// 검색어가 없으면 alert()
// 검색어가 있으면 하단의 actionForm 안 keyword value 값으로 삽입
// form submit()
const search = document.querySelector("#btn_search");
search.addEventListener("click",(e)=>{
    e.preventDefault();
    const keyword = document.querySelector("#top_keyword");
    if(keyword.value ==""){
        alert("검색어를 입력해 주세요");
        top_keyword.focus();
        return;
    }

    document.querySelector("#keyword").value=top_keyword.value;
    document.querySelector("#actionForm").submit();
})
// 정렬 기준 변화 시 값을 가져와서
// actionForm page=1 로 변경
// actionForm sort 에 값 변경한 후 actionForm 전송


document.querySelector(".so").addEventListener("change",(e)=>{
    const sort=e.target.value;
    document.querySelector("#page").value=1;
    document.querySelector("#sort").value=sort;
    document.querySelector("#actionForm").submit();
});

// 제목 클릭 시 
// a 태그 중지, href 값 가져오기
// actionForm 의 action 값을 가져온 href 로 변경 후 actionForm submit
const titles=document.querySelectorAll(".text-decoration-none");

titles.forEach((title)=>{

    title.addEventListener("click",(e)=>{
        e.preventDefault();

        let actionForm = document.querySelector("#actionForm");
        actionForm.action=e.target.href;
        actionForm.submit();
        
    });
});
