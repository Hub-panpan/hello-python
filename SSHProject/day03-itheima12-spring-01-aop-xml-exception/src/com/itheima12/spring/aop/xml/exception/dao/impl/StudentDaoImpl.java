package com.itheima12.spring.aop.xml.exception.dao.impl;

import com.itheima12.spring.aop.xml.exception.dao.StudentDao;

public class StudentDaoImpl implements StudentDao{
	public void saveStudent() throws Exception{
		// TODO Auto-generated method stub
		throw new RuntimeException("afdasdf");
	}
}
