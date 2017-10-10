package com.itheima12.spring.aop.xml.exception.service.impl;

import com.itheima12.spring.aop.xml.exception.dao.PersonDao;
import com.itheima12.spring.aop.xml.exception.service.PersonService;

public class PersonServiceImpl implements PersonService{
	private PersonDao personDao;

	public PersonDao getPersonDao() {
		return personDao;
	}

	public void setPersonDao(PersonDao personDao) {
		this.personDao = personDao;
	}

	public void savePerson() {
		// TODO Auto-generated method stub
		this.personDao.savePerson();
	}

	public void updatePerson() {
		// TODO Auto-generated method stub
		this.personDao.updatePerson();
	}
	
	
}
