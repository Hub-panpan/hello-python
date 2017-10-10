package com.itheima12.spring.aop.xml.exception.service.impl;

import com.itheima12.spring.aop.xml.exception.dao.StudentDao;
import com.itheima12.spring.aop.xml.exception.service.StudentService;

public class StudentServiceImpl implements StudentService{
	private StudentDao studentDao;

	public StudentDao getStudentDao() {
		return studentDao;
	}

	public void setStudentDao(StudentDao studentDao) {
		this.studentDao = studentDao;
	}

	public void savePerson() throws Exception{
		this.studentDao.saveStudent();
	}
}
