package com.itheima12.spring.aop.xml.exception.dao.impl;

import com.itheima12.spring.aop.xml.exception.dao.PersonDao;

public class PersonDaoImpl implements PersonDao{

	public void savePerson() {
		// TODO Auto-generated method stub
		int a = 1/0;
	}

	public void updatePerson() {
		// TODO Auto-generated method stub
		Long.parseLong("aaa");
	}

}
