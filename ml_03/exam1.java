// stu_id, stu_name, stu_python, stu_spark, stu_r
// 2023_201, 정형돈, 100, 99, 88

// 데이터를 넣는 스프링 웹
// mapper클래스로 작성

seq1 = 'java/~domain - Studnets(class)'
// package com.team2.domain;

// import lombok.Data;

// @Data
// public class Students {

// 	private String stuId;			// 학생번호
// 	private String stuName;			// 학생이름
// 	private int stuPython;			// Python점수
// 	private int stuSpark;			// Spark점수
// 	private int stuR;				// R점수
	
// }

seq2 = 'java/~mapper - StudentMapper(interface)'
// java/com.team2.mapper
// StudentMapper.java
// package com.team2.mapper;

// import org.apache.ibatis.annotations.Mapper;

// import com.team2.domain.Students;

// @Mapper
// public interface StudentMapper {
	
// 	// 학생 정보 등록
// 	public int stuInfo(Students student) throws Exception;
	
	
// }

seq3 = 'resources/~mapper - StudentMapper(xml)'
// resources/com.team2.mapper
// StudentMapper.xml
// <!DOCTYPE mapper
//     PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
//     "https://mybatis.org/dtd/mybatis-3-mapper.dtd">

// <mapper namespace="com.team2.mapper.StudentMapper">

// 	<!-- 학생 정보 등록 -->
// 	<insert id="stuInfo">
// 		INSERT INTO students (stu_id, stu_name, stu_python, stu_spark, stu_r)
// 		VALUES (SEQ_USER.nextval, #{stuId}, #{stuName}, #{stuPython}, #{stuSpark}, #{stuR})
// 	</insert>

	
// </mapper>
