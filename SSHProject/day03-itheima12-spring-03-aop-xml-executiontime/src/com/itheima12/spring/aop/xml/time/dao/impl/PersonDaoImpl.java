package com.itheima12.spring.aop.xml.time.dao.impl;

import com.itheima12.spring.aop.xml.time.dao.PersonDao;

public class PersonDaoImpl implements PersonDao{
//实现personDAO 接口
	public void savePerson(){
		try {
			//程序执行时间太快了 所以让程序睡一会  数据库那一层就没写
			Thread.sleep(3000L);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		System.out.println("save person");
	}
}
