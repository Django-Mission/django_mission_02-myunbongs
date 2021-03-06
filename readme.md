# Basic Mission


<aside>
💡 사용자와 소통창구, 고객센터 앱과 FAQ 모델 만들기

</aside>

### 미션 내용 : 고객센터 앱과 FAQ 모델 만들기

- 사용자에게 자주묻는질문 제공을 위한 고객센터앱, 자주묻는질문 모델 생성

### 목표

- 장고 ORM Models, Fields에 대한 이해

### 요구사항

- 고객센터 앱 생성
    - 앱명 : `support`
- FAQ 모델 생성
    - 모델명 : `Faq`
    - 필드 : 질문, 카테고리, 답변, 생성자, 생성일시, 최종 수정자, 최종 수정일시


### 동작 화면

https://user-images.githubusercontent.com/62318430/164023317-25278948-6795-40ef-878a-5b1597c5db84.mov

<img width="1440" alt="image" src="https://user-images.githubusercontent.com/62318430/164025623-ceb7acc5-2a28-453d-9b8a-877093b01230.png">


---


# Advanced Mission


고객센터 1:1 문의, 답글 모델 만들기

### 미션 내용 : 고객센터 앱에 1:1 문의, 답변 모델 만들기

### 목표

- 예시 화면 기반의 모델링 진행
    - 모델링 : 어떠한 데이터를 저장할 것인지 판단하여 모델 생성, 구성하는 작업
- 데이터베이스, 모델 관계 구성 이해

### 요구사항

- 1:1 문의, 답변 모델 생성
- 1:1 문의 모델 화면, 모델명 : `Inquiry`
- 답변 모델 생성, 모델명 : `Answer`
    - 답변 모델 필드 : 답변 내용, 참조 문의글, 생성자, 생성 일시, 최종 수정자, 최종 수정 일시
- 문의와 답변은 1 - N 관계 구성
    - 문의 1 - 답변 N

### 동작 화면 

https://user-images.githubusercontent.com/62318430/164023487-0efae27f-eeff-4847-88e4-a6eae126a7da.mov

<img width="1440" alt="image" src="https://user-images.githubusercontent.com/62318430/164025430-d88f6b15-3baf-4e11-961a-3e0ec6e67baa.png">


---
