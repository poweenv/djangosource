// delete 클래스명 이용
// 삭제 클릭 시
// a태그 중지
// confirm("정말로 삭제하시겠습니까?")
// 확인 클릭시 href 지정한 경로로 이동

// document.querySelector(".delete").addEventListener("click",(e)=>{
//     e.preventDefault();

//     if(confirm("정말로 삭제하시겠습니까?")){
//         location.href= e.target.href;
//     };
// });

const deleteAll=document.querySelectorAll(".delete");
deleteAll.forEach((item)=>{
    item.addEventListener("click",(e)=>{
        e.preventDefault();
        if(confirm("정말로 삭제하시겠습니까?")){
            location.href= e.target.href;
        }
    });
});

// 추천 버튼 클릭 시
// a 태그 중지 confirm 창 
const vote = document.querySelectorAll(".recommand");
vote.forEach((item)=>{
    item.addEventListener("click",(e)=>{
        e.preventDefault();
        
        if(confirm("추천 하시겠습니까?")){
            location.href = e.target.href;
        }
    });
});

// 목록으로 버튼 클릭 시 
// actionForm submit
document.querySelector(".btn-sm").addEventListener("click",(e)=>{
    e.preventDefault();
    document.querySelector("#actionForm").submit();
    
})