package com.itheima12.spring.aop.xml.transaction;

import org.junit.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

/**
 * 原理：
 *    1、当spring容器启动的时候，加载两个bean,对两个bean进行实例化
 *    2、当spring容器对配置文件解析到<aop:config>的时候
 *    3、把切入点表达式解析出来，按照切入点表达式匹配spring容器内容的bean
 *    4、如果匹配成功，则为该bean创建代理对象
 *    5、当客户端利用context.getBean获取一个对象时，如果该对象有代理对象，则返回代理对象
 *         如果没有代理对象，则返回对象本身
 * @author zd
 *
 */
public class TransactionTest {
	@Test
	public void testTransaction(){
		ApplicationContext context = 
				new ClassPathXmlApplicationContext("applicationContext.xml");
		PersonDao personDao = (PersonDao)context.getBean("personDao");
		personDao.savePerson();
	}
}
